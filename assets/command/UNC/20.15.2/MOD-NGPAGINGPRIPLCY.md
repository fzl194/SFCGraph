---
id: UNC@20.15.2@MMLCommand@MOD NGPAGINGPRIPLCY
type: MMLCommand
name: MOD NGPAGINGPRIPLCY（修改5G寻呼优先级策略参数配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGPAGINGPRIPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- 寻呼优先级策略参数配置
status: active
---

# MOD NGPAGINGPRIPLCY（修改5G寻呼优先级策略参数配置）

## 功能

**适用NF：AMF**

该命令用于修改5G寻呼优先级策略参数配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLCYIDX | 策略索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在AMF内唯一标识一条寻呼优先级策略。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用寻呼优先级的数据网络名称（DNN）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用寻呼优先级策略的ARP优先级等级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| PAGINGPRIORITY | 寻呼优先级等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼优先级等级。数值越小，表示NG-RAN寻呼用户的优先等级越高。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGPAGINGPRIPLCY]] · 5G寻呼优先级策略参数配置（NGPAGINGPRIPLCY）

## 使用实例

修改策略索引为1的用户寻呼优先级修改为1，执行如下命令：

```
MOD NGPAGINGPRIPLCY: PLCYIDX=1, PAGINGPRIORITY=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NGPAGINGPRIPLCY.md`
