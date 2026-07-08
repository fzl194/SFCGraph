---
id: UDG@20.15.2@MMLCommand@ADD PRINETPOLICY
type: MMLCommand
name: ADD PRINETPOLICY（添加专网控制策略）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: PRINETPOLICY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- 专网策略配置
- 专网控制策略
status: active
---

# ADD PRINETPOLICY（添加专网控制策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加一条专网控制策略。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 请在对接UAC服务器的专网设备上进行配置，其它设备上请勿配置该命令。
- UAC开关由关到开场景下仅对新流生效，老流不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：1、 输入的APN名称需要满足APN名称的取值范围。2、 该参数使用ADD APN命令配置生成。 |
| DNAI | 数据网络接入标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络接入标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。名称中不能包含空格，不区分大小写。<br>默认值：无<br>配置原则：输入的DNAI名称需要符合DNAI命名规则。 |
| SINGLENETACCSW | 单网通功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否使能单网通功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PRINETPOLICY]] · 专网控制策略（PRINETPOLICY）

## 使用实例

- 配置一条专网控制策略，APN为“test”，不填写DNAI参数，并且使能该策略：
  ```
  ADD PRINETPOLICY: APN="test", SINGLENETACCSW=ENABLE;
  ```
- 配置一条专网控制策略，APN为“test1”，DNAI为“123456”，不使能该策略：
  ```
  ADD PRINETPOLICY: APN="test1", DNAI="123456", SINGLENETACCSW=DISABLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加专网控制策略（ADD-PRINETPOLICY）_27889295.md`
