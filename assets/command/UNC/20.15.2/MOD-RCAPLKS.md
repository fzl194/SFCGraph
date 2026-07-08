---
id: UNC@20.15.2@MMLCommand@MOD RCAPLKS
type: MMLCommand
name: MOD RCAPLKS（修改注册中心链路集）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: RCAPLKS
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
- 注册中心管理
status: active
---

# MOD RCAPLKS（修改注册中心链路集）

## 功能

**适用NF：SMSF**

此命令用于修改注册中心链路集配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路集的索引。<br>数据来源：本端规划<br>取值范围：0~1<br>默认值：无 |
| LSN | 链路集名 | 可选必选说明：可选参数<br>参数说明：该参数用于指定链路集名称。<br>数据来源：整网规划<br>取值范围： 字符串类型，输入长度范围为0~63 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RCAPLKS]] · 注册中心链路集（RCAPLKS）

## 使用实例

1. 修改链路集索引为0的注册中心链路集配置，可以用如下命令：
  ```
  MOD RCAPLKS: LSX=0, LSN="huawei";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-RCAPLKS.md`
