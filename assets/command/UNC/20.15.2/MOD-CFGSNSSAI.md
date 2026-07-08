---
id: UNC@20.15.2@MMLCommand@MOD CFGSNSSAI
type: MMLCommand
name: MOD CFGSNSSAI（修改支持的S-NSSAI）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CFGSNSSAI
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- S-NSSAI配置管理
status: active
---

# MOD CFGSNSSAI（修改支持的S-NSSAI）

## 功能

**适用NF：NSSF**

该命令用于修改NSSF支持的S-NSSAI列表。

## 注意事项

- 该命令执行后立即生效。

- 该命令会修改支持的S-NSSAI列表。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NSSF上均需执行此命令，且配置参数一致。
- 该命令中相同MCC、MNC、SST下SDSTART与SDEND范围不能存在交集，该规则在配置SD时不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| SST | 切片服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于描述切片服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：<br>SD与SD区间配置二选一，不能同时使用。SD、SDSTART以及SDEND都为空时SD会被自动填充为FFFFFF。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于描述优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |
| ISACTIVE | 激活状态 | 可选必选说明：可选参数<br>参数含义：该参数用于描述切片的激活状态。<br>数据来源：全网规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| SDSTART | 切片细分标识区间的起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片细分标识区间的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：<br>SD与SD区间配置二选一，不能同时使用。<br>SDSTART与SDEND必须同时有值或者同时为空。 |
| SDEND | 切片细分标识区间的结束值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片细分标识区间的结束值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：<br>SD与SD区间配置二选一，不能同时使用。<br>SDSTART与SDEND必须同时有值或者同时为空。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CFGSNSSAI]] · 支持的S-NSSAI（CFGSNSSAI）

## 使用实例

- 假如运营商希望将已有的INDEX为1记录修改为MCC为"460"、MNC为"03"、SST为1、SD为"010101"、ISACTIVE为TRUE，执行下列命令。
  ```
  MOD CFGSNSSAI: INDEX=1, MCC="460", MNC="03", SST=1, SD="010101", ISACTIVE=TRUE;
  ```
- 假如运营商希望将已有的INDEX为1记录修改为MCC为"460"、MNC为"03"、SST为1、ISACTIVE为TRUE、SDSTART为"010101"、SDEND为"111111"，执行下列命令。
  ```
  MOD CFGSNSSAI: INDEX=1, MCC="460", MNC="03", SST=1, ISACTIVE=TRUE, SDSTART="010101", SDEND="111111";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-CFGSNSSAI.md`
