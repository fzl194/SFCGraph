---
id: UNC@20.15.2@MMLCommand@TST NFNOTIFY
type: MMLCommand
name: TST NFNOTIFY（测试NRF通知）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: NFNOTIFY
command_category: 调测类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF业务调测
status: active
---

# TST NFNOTIFY（测试NRF通知）

## 功能

**适用NF：NRF**

该命令用于测试当NF实例Profile信息变更时，NRF是否按照订阅关系通知其他NF实例。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示测试需要触发变更的NF实例标识。可以通过DSP REGNFINSTACE命令查询。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |
| PATCHSTR | Patch信息 | 可选必选说明：必选参数<br>参数含义：该参数表示测试的NF实例的Patch变更信息，按照JSON格式输入。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是0~5120。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [测试NRF通知（NFNOTIFY）](configobject/UNC/20.15.2/NFNOTIFY.md)

## 使用实例

当需要测试NF实例标识为af-1，Patch信息为"{"op":5,"path":"/nsiList/1","value":"'nsiList3'"}"，NRF对订阅此消息的其他NF的通知情况时，配置此命令。

```
TST NFNOTIFY: NFINSTANCEID="af-1", PATCHSTR="[{\"op\":5,\"path\":\"/nsiList/1\",\"value\":\"\\\"nsiList3\\\"\"}]";
%%TST NFNOTIFY: NFINSTANCEID="af-1", PATCHSTR="[{\"op\":5,\"path\":\"/nsiList/1\",\"value\":\"\\\"nsiList3\\\"\"}]";%%
RETCODE = 0  操作成功

结果如下
------------------------
通知结果  =  {
    "NRF Notify NFInstance List": [
        {
            "SubscriptionId": "0004008cf47fe2f360084ce9bff8db09520cf82c",
            "NfStatusNotificationUri": "http://10.0.0.0:1234/nnrf-nfm/v1/nf-instances/bf-1"
        }
    ]
}
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试NRF通知（TST-NFNOTIFY）_09652531.md`
