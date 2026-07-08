---
id: UNC@20.15.2@MMLCommand@LST NFSRVNTFSUBS
type: MMLCommand
name: LST NFSRVNTFSUBS（查询服务回调信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFSRVNTFSUBS
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF服务订阅管理
status: active
---

# LST NFSRVNTFSUBS（查询服务回调信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于查询服务实例的回调信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定回调信息对应的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定回调信息对应的服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- 本参数与ADD NFSERVICE命令中的SRVINSTANCEID值一致时生效。<br>- 本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，Service_Instance_0。 |
| NTFICATIONTYPE | 通知类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定回调URI通知类型。<br>数据来源：全网规划<br>取值范围：<br>- NtfInvalid（NtfInvalid）<br>- N1Msg（N1Msg）<br>- N2Info（N2Info）<br>- LocNty（LocNty）<br>- DataRmvNtf（DataRmvNtf）<br>- DataChgNtf（DataChgNtf）<br>- NtfMax（NtfMax）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFSRVNTFSUBS]] · 服务回调信息（NFSRVNTFSUBS）

## 使用实例

运营商A需要查询NFINSTANCENAME为AMF_Instance_0，SRVINSTANCEID为Service_Instance_0的服务实例的回调信息。

```
%%LST NFSRVNTFSUBS: NFINSTANCENAME="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0";%%
RETCODE = 0  操作成功

结果如下
--------
  NF实例名称  =  AMF_Instance_0
服务实例标识  =  Service_Instance_0
    通知类型  =  N1Msg
     回调URI  =  http://192.168.0.1:80/callbackFunc
  N1消息类别  =  EN1Invalid
  N2消息类别  =  EN2Invalid
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务回调信息（LST-NFSRVNTFSUBS）_09652956.md`
