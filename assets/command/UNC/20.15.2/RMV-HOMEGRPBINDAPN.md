---
id: UNC@20.15.2@MMLCommand@RMV HOMEGRPBINDAPN
type: MMLCommand
name: RMV HOMEGRPBINDAPN（删除Home Group和APN的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HOMEGRPBINDAPN
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- Home Group绑定APN
status: active
---

# RMV HOMEGRPBINDAPN（删除Home Group和APN的绑定关系）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于删除APN与Home Group的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 该命令不指定Home Group时，表示解除指定APN与所有已绑定Home Group的绑定关系。
- 该命令指定Home Group时，表示解除指定APN与指定Home Group的绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| HOMEGROUPINDX | Home Group编号 | 可选必选说明：可选参数<br>参数含义：该参数用来设置Home Group的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>该参数使用ADD HOMEGROUP命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HOMEGRPBINDAPN]] · Home Group和APN的绑定关系（HOMEGRPBINDAPN）

## 使用实例

- 删除“APN”为“huawei.com”，“Home Group编号”为“1”的Home Group和APN的绑定关系配置：
  ```
  LST HOMEGRPBINDAPN: APN="huaweit.com", HOMEGROUPINDX=1;
  ```
- 删除“APN”为“huawei.com”的全部Home Group和APN的绑定关系配置：
  ```
  LST HOMEGRPBINDAPN: APN="huaweit.com";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Home-Group和APN的绑定关系（RMV-HOMEGRPBINDAPN）_42853268.md`
