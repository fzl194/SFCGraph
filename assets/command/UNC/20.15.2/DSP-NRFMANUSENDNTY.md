---
id: UNC@20.15.2@MMLCommand@DSP NRFMANUSENDNTY
type: MMLCommand
name: DSP NRFMANUSENDNTY（显示手动发送订阅通知结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFMANUSENDNTY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF手动发送订阅通知
status: active
---

# DSP NRFMANUSENDNTY（显示手动发送订阅通知结果）

## 功能

**适用NF：NRF**

此命令用于查询手动向NF发送的订阅通知的发送结果。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CALLBACKURI | 通知地址 | 可选必选说明：可选参数<br>参数含义：该参数表示通知发往的目的NF回调URI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~512。<br>默认值：无<br>配置原则：无 |
| SUBID | 订阅标识 | 可选必选说明：可选参数<br>参数含义：该字段表示订阅者的订阅标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~48。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFMANUSENDNTY]] · 操作手动发送订阅通知（NRFMANUSENDNTY）

## 使用实例

显示手动发送的订阅通知结果。

```
%%DSP NRFMANUSENDNTY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  通知地址  =  http://10.70.1.118:5164/nnrf-nfm/v1/nf-instances/ff02-1
  订阅标识  =  000200050b16cec9bd65491681cb88775ca9ded0
通知响应码  =  204
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NRFMANUSENDNTY.md`
