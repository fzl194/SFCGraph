---
id: UNC@20.15.2@MMLCommand@MOD DNAIINFO
type: MMLCommand
name: MOD DNAIINFO（修改DNAI信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DNAIINFO
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI管理
- DNAI信息管理
status: active
---

# MOD DNAIINFO（修改DNAI信息）

## 功能

**适用NF：SMF、PGW-C**

该命令用于修改DNAI信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SHUNTDIRECT | 分流方向 | 可选必选说明：可选参数<br>参数含义：该参数用于控制分流的方向。<br>数据来源：全网规划<br>取值范围：<br>- “NORMAL（正向）”：正向分流<br>- “REVERSE（反向）”：反向分流<br>默认值：无<br>配置原则：<br>该参数配置为正向分流，园区业务分流到辅锚点；<br>该参数配置为反向分流，园区业务分流到主锚点。 |
| SHUNTLOC | 分流位置 | 可选必选说明：可选参数<br>参数含义：该参数用于指示DNAI的分流位置。<br>数据来源：全网规划<br>取值范围：<br>- “HOME（归属地）”：归属地分流<br>默认值：无<br>配置原则：<br>该参数对I-SMF不生效。 |
| ALWAYSSHUNTSW | Always分流开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制DNAI是否支持Always分流。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：不支持Always分流<br>- “ENABLE（使能）”：支持Always分流<br>默认值：无<br>配置原则：<br>开关默认关闭，DNAI不支持Always分流；<br>当DNAI规划为整网范围内生效时，需打开Always分流开关。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNAIINFO]] · DNAI信息（DNAIINFO）

## 使用实例

修改cmnet_dnai的分流方向为正向分流，分流位置为归属地分流，关闭Always分流开关

```
MOD DNAIINFO: DNAI="cmnet_dnai", SHUNTDIRECT=NORMAL, SHUNTLOC=HOME, ALWAYSSHUNTSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DNAIINFO.md`
