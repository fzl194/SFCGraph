---
id: UNC@20.15.2@MMLCommand@MOD NGPRDREGTIMEDNN
type: MMLCommand
name: MOD NGPRDREGTIMEDNN（修改基于DNN的周期性注册时长配置）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD NGPRDREGTIMEDNN（修改基于DNN的周期性注册时长配置）

## 功能

![](修改基于DNN的周期性注册时长配置（MOD NGPRDREGTIMEDNN）_21742357.assets/notice_3.0-zh-cn_2.png)

该命令仅建议对低功耗用户签约的DNN进行配置，如果DNN配置错误可能会对其它用户造成影响。

**适用NF：AMF**

该命令用于修改基于DNN的周期性注册时长配置。

## 注意事项

- 该命令执行后立即生效。

- 当修改本配置时，T3512在下一次用户注册时生效，移动可达定时器实时生效。
- UE请求的T3512暂不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNI | DNN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定周期性注册时长的目标DNN网络标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>- “*”表示通配符，如果DNNNI为“*”，表示所有DNNNI都支持此配置的周期性注册时长。<br>- 使用DNNNI参数的配置值在用户签约数据smfSelData中所有切片下的DNN列表中进行匹配。 |
| TIMEPLCY | 周期性注册时长获取策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定周期性注册时长获取的策略。<br>数据来源：全网规划<br>取值范围：<br>- “UDMSUB（签约数据优先）”：若UDM签约subsRegTimer且小于本配置的移动可达定时器，则签约有效；否则AMF取本配置中的T3512。<br>- “LOCAL（本地配置优先）”：AMF取本配置中的T3512。<br>默认值：无<br>配置原则：无 |
| T3512 | T3512(min) | 可选必选说明：可选参数<br>参数含义：该参数用于设置本地配置的周期性注册时长；如果不配置，则本地配置取自SET NGMMPARA命令中的T3512。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~780。<br>默认值：无<br>配置原则：<br>该定时器的取值范围为离散值，根据3gpp规范24.008的10.5.7.4a章节中定义的取值规则如下：<br>当取值为1min，T3512信元的编码单位为2s；<br>当范围为2min-15min，编码单位为30s；<br>当范围为16min-31min，编码单位为1min；<br>当范围为32min-310min，编码单位为10min；<br>当范围为311min-780min，编码单位为1hour。<br>例如：当取值为2min时，T3512信元值为4，编码单位为30s。增加T3512(min)的值会减少CM-CONNECTED注册用户数、增加CM-IDLE注册用户数、减少周期性注册更新请求次数、增加寻呼次数。 |
| RCHTMR | 移动可达定时器(min) | 可选必选说明：可选参数<br>参数含义：该定时器用于监测UE是否发起周期性注册更新流程。该定时器在UE的NAS信令连接释放时启动，在NAS信令连接建立时停止；超时后，如果UE还没有发起周期性注册更新流程，则启动不可达用户隐式去注册定时器（IMDTCHTMR），取自SET NGMMPARA命令中的IMDTCHTMR。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是2~792，单位是分钟。<br>默认值：无<br>配置原则：<br>- 此定时器时长应大于“T3512(min)”时长。<br>- 增加“移动可达定时器(min)”的值会增加CM-IDLE注册用户数、减少DEREGISTERED态用户数、增加寻呼次数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPRDREGTIMEDNN]] · 基于DNN的周期性注册时长配置（NGPRDREGTIMEDNN）

## 使用实例

修改DNNNI为“abc”、周期性注册时长获取策略为本地配置优先、周期性注册时长780分钟、移动可达定时器792分钟的配置，执行如下命令：

```
MOD NGPRDREGTIMEDNN:DNNNI="abc",TIMEPLCY=LOCAL,T3512=780,RCHTMR=792;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于DNN的周期性注册时长配置（MOD-NGPRDREGTIMEDNN）_21742357.md`
