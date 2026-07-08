---
id: UNC@20.15.2@MMLCommand@ADD TMGIRNG
type: MMLCommand
name: ADD TMGIRNG（增加TMGI号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TMGIRNG
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- MB-SMF TMGI配置管理
status: active
---

# ADD TMGIRNG（增加TMGI号段）

## 功能

**适用NF：SMF**

该命令用来增加TMGI号段。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入50条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。仅支持0-9的数字，所有配置下仅支持同一个MCC、MNC组合。<br>默认值：无<br>配置原则：<br>配置时应与基站支持的MCC保持一致。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。仅支持0-9的数字，所有配置下仅支持同一个MCC、MNC组合。<br>默认值：无<br>配置原则：<br>配置时应与基站支持的MNC保持一致。 |
| MBSIDRNGSTART | MBS Service ID区域起点值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定组播广播服务标识区域起点值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是8。字符串类型，长度为8位。 必须是0x/X开头的十六进制数，仅支持输入0x/X、0-9、a-f/A-F，字母不区分大小写，取值范围0x000000~0xFFFFFF。<br>默认值：无<br>配置原则：<br>MBSIDRNGSTART一定要小于等于MBSIDRNGEND。 |
| MBSIDRNGEND | MBS Service ID区域结束值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MBS Service ID区域结束值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是8。字符串类型，长度为8位。 必须是0x/X开头的十六进制数，仅支持输入0x/X、0-9、a-f/A-F，字母不区分大小写，取值范围0x000000~0xFFFFFF。<br>默认值：无<br>配置原则：<br>MBSIDRNGSTART一定要小于等于MBSIDRNGEND。 |
| ISSTATIC | 是否静态TMGI号段 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当前TMGI号段是否为静态TMGI号段。<br>数据来源：全网规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>当参数ISSTATIC设置为TRUE时，表示当前TMGI号段不再作为MBSMF可分配的TMGI号段，以对端AF携带的TMGI中的PLMN为准，不再使用当前配置中的MCC和MNC参数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TMGIRNG]] · TMGI号段（TMGIRNG）

## 使用实例

- 当需要增加MCC为460，MNC为03，MBSSERVICEIDSTART为0x000001，MBSSERVICEIDEND为0x000002的TMGI号段时，执行如下命令：
  ```
  ADD TMGIRNG: MCC="460", MNC="03", MBSIDRNGSTART="0x000001", MBSIDRNGEND="0x000002";
  ```
- 当需要增加MCC为460，MNC为03，MBSSERVICEIDSTART为0x000001，MBSSERVICEIDEND为0x000002，ISSTATIC为TRUE的TMGI号段时，执行如下命令：
  ```
  ADD TMGIRNG: MCC="460", MNC="03", MBSIDRNGSTART="0x000001", MBSIDRNGEND="0x000002", ISSTATIC=TRUE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TMGIRNG.md`
