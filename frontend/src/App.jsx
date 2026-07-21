import { useState } from "react";
import "./index.css";

import mine from "./assets/mine.png";
import star from "./assets/star.png";

const SIZE = 25;

export default function App() {
  const [mines, setMines] = useState(3);
  const [board, setBoard] = useState(Array(SIZE).fill("hidden"));

  function generateBoard() {
    const arr = Array(SIZE).fill("star");

    const positions = [];

    while (positions.length < mines) {
      const random = Math.floor(Math.random() * SIZE);

      if (!positions.includes(random)) {
        positions.push(random);
        arr[random] = "mine";
      }
    }

    setBoard(arr);
  }

  return (
    <div className="app">

      {/* Фон */}
      <div className="backgroundGlow"></div>

      {/* Логотип */}
      <div className="logo">

        <div className="logoIcon">💣</div>

        <div className="logoText">
          Hunter
          <span>Mines</span>
        </div>

      </div>

      {/* Игровое поле */}
      <div className="board">

        {board.map((cell, index) => (

          <div className="cell" key={index}>

            {cell !== "hidden" && (

              <img
                src={cell === "mine" ? mine : star}
                className={`icon ${
                  cell === "mine"
                    ? "mineIcon"
                    : "starIcon"
                }`}
                alt=""
              />

            )}

          </div>

        ))}

      </div>

      {/* Панель ловушек */}
      <div className="trapsPanel">

        <button
          className="arrow"
          onClick={() =>
            setMines(Math.max(1, mines - 1))
          }
        >
          −
        </button>

        <div className="trapCenter">

          <div className="trapTitle">
            ЛОВУШЕК
          </div>

          <div className="trapValue">
            {mines}
          </div>

        </div>

        <button
          className="arrow"
          onClick={() =>
            setMines(Math.min(24, mines + 1))
          }
        >
          +
        </button>

      </div>

      {/* Кнопка */}
      <button
        className="play"
        onClick={generateBoard}
      >
        🎮 ИГРАТЬ
      </button>

    </div>
  );
}