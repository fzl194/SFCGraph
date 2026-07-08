---
id: UNC@20.15.2@MMLCommand@ADD RCAPLKS
type: MMLCommand
name: ADD RCAPLKS（增加注册中心链路集）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD RCAPLKS（增加注册中心链路集）

## 功能

**适用NF：SMSF**

此命令用于新增注册中心链路集配置。一个注册中心最多支持一个链路集。

## 注意事项

- 该命令执行后立即生效。
- 整系统最多配置2个。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路集的索引。<br>数据来源：本端规划<br>取值范围：0~1<br>默认值：无<br>配置原则：增加链路集时，链路集索引建议从小到大配置。 |
| RCN | 注册中心号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定注册中心索引。<br>数据来源：整网规划<br>取值范围：0~1<br>默认值：无<br>配置原则：须先在<br>[ADD RCENTER](增加注册中心 (ADD RCENTER)_45318842.md)<br>中配置取值相同的<br>“RCX”<br>参数。 |
| LSN | 链路集名 | 可选必选说明：可选参数<br>参数说明：该参数用于指定链路集名称。<br>数据来源：整网规划<br>取值范围： 字符串类型，输入长度范围为0~63<br>默认值： noname<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RCAPLKS]] · 注册中心链路集（RCAPLKS）

## 使用实例

1. 添加注册中心链路集配置，链路集索引为“0”，注册中心号为“0”，链路集名为“huawei”：
  ```
  ADD RCAPLKS: LSX=0, RCN=0, LSN="huawei";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-RCAPLKS.md`
