---
id: UNC@20.15.2@MMLCommand@LST N7RCVATTRCTRL
type: MMLCommand
name: LST N7RCVATTRCTRL（查询N7接收信元处理控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N7RCVATTRCTRL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- N7接收分发控制
status: active
---

# LST N7RCVATTRCTRL（查询N7接收信元处理控制）

## 功能

**适用NF：SMF**

此命令用于查询N7接口接收到的消息中部分信元的处理方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [N7接收信元处理控制（N7RCVATTRCTRL）](configobject/UNC/20.15.2/N7RCVATTRCTRL.md)

## 使用实例

查询N7RcvAttrCtrl的值。

```
%%LST N7RCVATTRCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
                 无PacketFilterUsage  =  不发送Packet Fliter给UE
                 修改QoSData关键属性  =  修改QoSFlow
                 缺省QosRule生成方法  =  PCC规则
基于Notify消息ResourceURI触发PCF重选  =  不使能
            SCELL_CH是否允许上报NCGI  =  不使能
          是否使用PCF返回的URI进行转发 = 不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N7接收信元处理控制（LST-N7RCVATTRCTRL）_09651331.md`
