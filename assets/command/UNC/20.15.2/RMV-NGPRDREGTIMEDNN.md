---
id: UNC@20.15.2@MMLCommand@RMV NGPRDREGTIMEDNN
type: MMLCommand
name: RMV NGPRDREGTIMEDNN（删除基于DNN的周期性注册时长配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGPRDREGTIMEDNN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- 5G移动管理定时器
status: active
---

# RMV NGPRDREGTIMEDNN（删除基于DNN的周期性注册时长配置）

## 功能

![](删除基于DNN的周期性注册时长配置（RMV NGPRDREGTIMEDNN）_21742369.assets/notice_3.0-zh-cn_2.png)

该命令仅建议对低功耗用户签约的DNN进行配置，如果DNN配置错误可能会对其它用户造成影响。

**适用NF：AMF**

该命令用于删除基于DNN的周期性注册时长配置。

## 注意事项

- 该命令执行后立即生效。

- 当删除本配置时，T3512在下一次用户注册时生效，移动可达定时器实时生效。
- UE请求的T3512暂不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNI | DNN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定周期性注册时长的目标DNN网络标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>- “*”表示通配符，如果DNNNI为“*”，表示所有DNNNI都支持此配置的周期性注册时长。<br>- 使用DNNNI参数的配置值在用户签约数据smfSelData中所有切片下的DNN列表中进行匹配。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPRDREGTIMEDNN]] · 基于DNN的周期性注册时长配置（NGPRDREGTIMEDNN）

## 使用实例

删除DNNNI为“abc”的配置，执行如下命令：

```
RMV NGPRDREGTIMEDNN:DNNNI="abc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGPRDREGTIMEDNN.md`
