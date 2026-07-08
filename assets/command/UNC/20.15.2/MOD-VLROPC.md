---
id: UNC@20.15.2@MMLCommand@MOD VLROPC
type: MMLCommand
name: MOD VLROPC（修改VLR信令点）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: VLROPC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- VLR管理
status: active
---

# MOD VLROPC（修改VLR信令点）

## 功能

**适用NF：SMSF**

该命令用于修改VLR信令点配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | VLR信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VLR本局信令点索引。<br>数据来源：本端规划<br>取值范围：0~1。<br>默认值：无 |
| VLRNAME | 本局VLR名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本局信令点名。该字段需要和MME协商。<br>数据来源：本端规划<br>取值范围：<br>字符串类型，输入长度范围为0~32<br>默认值：noname |
| SSN | 子系统号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMSF本局信令点的主用信令点。<br>数据来源：本端规划<br>取值范围：<br>- “VLR(7)”<br>- “MSC(8)”<br>默认值：VLR(7) |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLROPC]] · VLR信令点（VLROPC）

## 使用实例

修改VLR本局信令点，本局信令点索引为1，子系统号为MSC：

```
MOD VLROPC: OPX=1, SSN=MSC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-VLROPC.md`
