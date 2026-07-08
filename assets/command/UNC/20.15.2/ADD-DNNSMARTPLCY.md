---
id: UNC@20.15.2@MMLCommand@ADD DNNSMARTPLCY
type: MMLCommand
name: ADD DNNSMARTPLCY（增加DNN智能分流配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DNNSMARTPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- DNN智能分流管理
- DNN智能分流开启策略
status: active
---

# ADD DNNSMARTPLCY（增加DNN智能分流配置）

## 功能

**适用NF：AMF**

该命令用于新增PDU会话创建使用的DNN智能分流参数配置，智能分流用户使用的DNN开启了专用SMF选择功能，会话创建时系统会选择专用锚点SMF。

## 注意事项

- 该命令执行后立即生效。

- 不配置命令，智能分流用户会话使用的DNN默认开启专用SMF选择功能。
- 配置该命令，以配置命令为准。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户会话创建使用的DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| SMFSELSW | 是否支持专用SMF选择 | 可选必选说明：必选参数<br>参数含义：该参数用于指定智能分流用户PDU会话创建时使用的DNN是否支持专用SMF选择。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNN智能分流配置（DNNSMARTPLCY）](configobject/UNC/20.15.2/DNNSMARTPLCY.md)

## 使用实例

DNN“huawei.com”开启专用SMF选择功能，执行如下命令：

```
ADD DNNSMARTPLCY: DNN="huawei.com", SMFSELSW=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DNN智能分流配置（ADD-DNNSMARTPLCY）_87520112.md`
