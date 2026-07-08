---
id: UNC@20.15.2@MMLCommand@MOD M3LE
type: MMLCommand
name: MOD M3LE（修改M3UA本地实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: M3LE
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA本地实体
status: active
---

# MOD M3LE（修改M3UA本地实体）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于修改M3UA本地实体配置数据。

## 注意事项

- 该命令执行后立即生效。
- 只能修改本地实体名。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LEX | 本地实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示准备修改的本地实体的索引。<br>数据来源：本端规划<br>取值范围：0~63<br>默认值：无<br>配置原则：无 |
| LEN | 本地实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本地实体名称，标识本地实体。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [M3UA本地实体（M3LE）](configobject/UNC/20.15.2/M3LE.md)

## 使用实例

将索引为1的M3UA本地实体名改为“Test_M3le1”：

```
MOD M3LE: LEX=1, LEN="Test_M3le1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改M3UA本地实体(MOD-M3LE)_26146314.md`
