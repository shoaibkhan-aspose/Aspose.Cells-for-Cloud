package com.aspose.cells.model;

import com.aspose.cells.model.FillFormat;
public class FillFormatResponse {
  private FillFormat FillFormat = null;
  private String Code = null;
  private String Status = null;
  /**
	 * getFillFormat
	 * Gets FillFormat
	 * @return FillFormat
	 */
  public FillFormat getFillFormat() {
    return FillFormat;
  }

	/**
	 * setFillFormat
	 * Sets FillFormat
	 * @param FillFormat FillFormat
	 */
  public void setFillFormat(FillFormat FillFormat) {
    this.FillFormat = FillFormat;
  }

  /**
	 * getCode
	 * Gets String
	 * @return Code
	 */
  public String getCode() {
    return Code;
  }

	/**
	 * setCode
	 * Sets String
	 * @param Code String
	 */
  public void setCode(String Code) {
    this.Code = Code;
  }

  /**
	 * getStatus
	 * Gets String
	 * @return Status
	 */
  public String getStatus() {
    return Status;
  }

	/**
	 * setStatus
	 * Sets String
	 * @param Status String
	 */
  public void setStatus(String Status) {
    this.Status = Status;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class FillFormatResponse {\n");
    sb.append("  FillFormat: ").append(FillFormat).append("\n");
    sb.append("  Code: ").append(Code).append("\n");
    sb.append("  Status: ").append(Status).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}

