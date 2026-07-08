---
id: UDG@20.15.2@MMLCommand@RTR BFDSESSSTAS
type: MMLCommand
name: RTR BFDSESSSTAS（清除BFD会话统计信息）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: BFDSESSSTAS
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- BFD管理
- BFD会话统计
status: active
---

# RTR BFDSESSSTAS（清除BFD会话统计信息）

## 功能

该命令用于清除BFD会话相关的统计计数信息。可以基于会话清除统计计数信息。

## 注意事项

- 该命令执行后立即生效。
- 清除后不可恢复计数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESETTYPE | 复位类型 | 可选必选说明：必选参数<br>参数含义：清除统计信息的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：所有BFD会话。<br>- DISCRIMINATOR：指定本地标识符的BFD会话。<br>默认值：无 |
| LOCALDISCR | 本地标识符 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RESETTYPE”配置为“DISCRIMINATOR”时为必选参数。<br>参数含义：清除单个会话的统计信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～49152。<br>默认值：无 |

## 操作的配置对象

- [BFD会话统计信息（BFDSESSSTAS）](configobject/UDG/20.15.2/BFDSESSSTAS.md)

## 使用实例

- 清空BFD所有会话的统计信息：
  ```
  RTR BFDSESSSTAS:RESETTYPE=ALL;
  ```
- 清空本地标识符为1222的会话统计信息：
  ```
  RTR BFDSESSSTAS:RESETTYPE=DISCRIMINATOR,LOCALDISCR=1222;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除BFD会话统计信息（RTR-BFDSESSSTAS）_50121530.md`
