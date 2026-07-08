---
id: UNC@20.15.2@MMLCommand@ADD USNRSVCMD5
type: MMLCommand
name: ADD USNRSVCMD5（增加预埋命令5）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: USNRSVCMD5
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 预埋命令
status: active
---

# ADD USNRSVCMD5（增加预埋命令5）

## 功能

**适用网元：MME**

该命令用于添加实现指定的功能所需要的命令名称以及对应的参数信息。

## 注意事项

无

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FUNNAME | 功能名称 | 可选必选说明：必选参数<br>参数含义：表示功能名称，类似普通的MML命令名<br>数据来源：本端规划<br>取值范围：字符串形式，区分大小写，字符串长度为1～31。<br>默认值：无 |
| FUNKEY | 功能KEY参数 | 可选必选说明：必选参数<br>参数含义：功能名称对应的KEY参数。<br>数据来源：本端规划<br>取值范围：字符串形式，区分大小写，字符串长度为1～31。<br>默认值：无 |
| STRPARA1 | 字符串参数1 | 可选必选说明：可选参数<br>参数含义：功能所需要的字符串参数1。<br>数据来源：本端规划<br>取值范围：字符串长度为1～63。<br>默认值：无 |
| STRPARA2 | 字符串参数2 | 可选必选说明：可选参数<br>参数含义：功能所需要的字符串参数2。<br>数据来源：本端规划<br>取值范围：字符串长度为1～63。<br>默认值：无 |
| STRPARA3 | 字符串参数3 | 可选必选说明：可选参数<br>参数含义：功能所需要的字符串参数3。<br>数据来源：本端规划<br>取值范围：字符串长度为1～63。<br>默认值：无 |
| INTPARA1 | 整型参数1 | 可选必选说明：可选参数<br>参数含义：功能所需要的整型参数1。<br>数据来源：本端规划<br>取值范围：整型数值<br>默认值：无 |
| INTPARA2 | 整型参数2 | 可选必选说明：可选参数<br>参数含义：功能所需要的整型参数2。<br>数据来源：本端规划<br>取值范围：整型数值<br>默认值：无 |
| INTPARA3 | 整型参数3 | 可选必选说明：可选参数<br>参数含义：功能所需要的整型参数3。<br>数据来源：本端规划<br>取值范围：整型数值<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USNRSVCMD5]] · 预埋命令5（USNRSVCMD5）

## 使用实例

想添加通过命令名称为MOD GLOBALVARIABLE来修改某个全局变量的值的功能，则可以执行以下命令：

ADD USNRSVCMD5: FUNNAME="MOD GLOBALVARIABLE", FUNKEY="TESTKEY", STRPARA1="asddas123", STRPARA2="asdA", STRPARA3="ASDFAS", INTPARA1=1231, INTPARA2=12312, INTPARA3=1231;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加预埋命令5-(ADD-USNRSVCMD5)_23195744.md`
