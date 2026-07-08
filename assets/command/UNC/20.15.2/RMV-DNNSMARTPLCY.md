---
id: UNC@20.15.2@MMLCommand@RMV DNNSMARTPLCY
type: MMLCommand
name: RMV DNNSMARTPLCY（删除DNN智能分流配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV DNNSMARTPLCY（删除DNN智能分流配置）

## 功能

**适用NF：AMF**

该命令用于删除会话创建使用的DNN智能分流配置。

## 注意事项

- 该命令执行后立即生效。

- 删除该配置，如果用户是智能分流用户则配置中的DNN默认支持专用SMF选择功能。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户会话创建使用的DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNNSMARTPLCY]] · DNN智能分流配置（DNNSMARTPLCY）

## 使用实例

删除DNN“huawei.com”智能分流配置，执行如下命令：

```
RMV DNNSMARTPLCY: DNN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DNNSMARTPLCY.md`
