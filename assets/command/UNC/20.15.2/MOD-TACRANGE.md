---
id: UNC@20.15.2@MMLCommand@MOD TACRANGE
type: MMLCommand
name: MOD TACRANGE（修改NF TAC区域信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: TACRANGE
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF TAC区域信息管理
status: active
---

# MOD TACRANGE（修改NF TAC区域信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于修改TAC区域信息的描述信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定索引标识，用于标识TAC区域。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示对TAC区域信息的描述，在运维中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TACRANGE]] · NF TAC区域信息（TACRANGE）

## 使用实例

运营商A要修改索引标识为1的TAC描述信息。

```
MOD TACRANGE: INDEX=1, DESC="SHANGHAI";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-TACRANGE.md`
