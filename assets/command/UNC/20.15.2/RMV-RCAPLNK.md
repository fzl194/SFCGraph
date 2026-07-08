---
id: UNC@20.15.2@MMLCommand@RMV RCAPLNK
type: MMLCommand
name: RMV RCAPLNK（删除注册中心链路）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RCAPLNK
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

# RMV RCAPLNK（删除注册中心链路）

## 功能

**适用NF：SMSF**

此命令用于删除注册中心链路配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路的索引。该参数用来在系统范围内部唯一标识一条Rcenter链路。<br>数据来源：整网规划<br>取值范围：0~1023<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RCAPLNK]] · 注册中心链路（RCAPLNK）

## 使用实例

1. 删除链路索引为0的注册中心链路配置，可以用如下命令：
  ```
  RMV RCAPLNK: LNK=0;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RCAPLNK.md`
