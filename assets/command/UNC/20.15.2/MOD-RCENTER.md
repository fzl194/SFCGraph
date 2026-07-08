---
id: UNC@20.15.2@MMLCommand@MOD RCENTER
type: MMLCommand
name: MOD RCENTER（修改注册中心）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: RCENTER
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

# MOD RCENTER（修改注册中心）

## 功能

**适用NF：SMSF**

此命令用于修改注册中心配置。在该命令中，系统通过“注册中心索引”参数来唯一标识一条中心注册记录。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RCX | 注册中心索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定注册中心的索引。<br>数据来源：本端规划<br>取值范围：0~1<br>默认值：无 |
| RCM | 注册中心名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定注册中心名称。<br>数据来源：整网规划<br>取值范围：字符串类型，输入长度范围为0~63<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RCENTER]] · 注册中心（RCENTER）

## 使用实例

1. 修改注册中心索引为0的注册中心配置，可以用如下命令：
  ```
  MOD RCENTER: RCX=0, RCM="huawei";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改注册中心-(MOD-RCENTER)_45159154.md`
