class ResizePosition
{
    static #center = "center";
    static #top = "top";
    static #right = "right";
    static #bottom = "bottom";
    static #left = "left";

    static get CENTER () { return this.#center }
    static get TOP () { return this.#top }
    static get RIGHT () { return this.#right }
    static get BOTTOM () { return this.#bottom }
    static get LEFT () { return this.#left }
}


module.exports = ResizePosition;