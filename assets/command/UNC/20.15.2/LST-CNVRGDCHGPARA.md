---
id: UNC@20.15.2@MMLCommand@LST CNVRGDCHGPARA
type: MMLCommand
name: LST CNVRGDCHGPARA（查询融合计费全局参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CNVRGDCHGPARA
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# LST CNVRGDCHGPARA（查询融合计费全局参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询融合计费全局参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [融合计费全局参数（CNVRGDCHGPARA）](configobject/UNC/20.15.2/CNVRGDCHGPARA.md)

## 使用实例

查询融合计费全局参数：

```
%%LST CNVRGDCHGPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
                   多UPF场景配额管理  =  独立配额
               漫游用户归属地QBC计费  =  不使能
            位置信息必选信元缺失处理  =  不携带
             ChargingDataRef生成方式  =  CHF生成ChargingDataRef
               携带Start Trigger开关  =  不使能
        IPv6地址Interface Identifier  =  INITITFID
                 RG级Trigger填写方式  =  不使能
                  离线RG时长计算方式  =  PACKETTRIGGERED
             基于GrantedUnit上报用量  =  不使能
        延时上报PDU级Trigger携带方式  =  PDU级不携带
            PDU级门限Trigger适用范围  =  在线计费用户&离线计费用户&融合计费用户
             RG级门限Trigger适用范围  =  离线计费用户&融合计费用户
               RG VT事件合并上报开关  =  不使能
           忽略CHF响应消息的信元列表  =  NULL
       CHF响应消息信元错误的处理动作  =  去活会话
Trigger中是否支持填写AbnormalRelease  =  使能
      控制Nchf消息中时间戳的计算方式  =  四舍五入
          删除动态规则是否通知用户面  =  使能
            忽略CHF下发的Trigger列表  =  NULL
                      无业务上报开关  =  使能
             去活等待更新消息响应开关 =  不使能
            忽略CHF下发非法Triggers  =  使能
            缓存未开启放通告警开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询融合计费全局参数（LST-CNVRGDCHGPARA）_09654403.md`
