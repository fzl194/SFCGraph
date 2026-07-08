---
id: UNC@20.15.2@MMLCommand@LST UPFPFCPPARA
type: MMLCommand
name: LST UPFPFCPPARA（查询UPF粒度PFCP参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFPFCPPARA
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- UPF粒度PFCP路径参数管理
status: active
---

# LST UPFPFCPPARA（查询UPF粒度PFCP参数）

## 功能

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于查询指定实例名称的UPF粒度PFCP参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFPFCPPARA]] · UPF粒度PFCP参数（UPFPFCPPARA）

## 使用实例

查询实例名称为“upf1”的UPF粒度PFCP参数

```
%%LST UPFPFCPPARA: UPFINSTANCEID="upf1";%%
RETCODE = 0  操作成功

结果如下
--------
                 UPF实例标识  =  upf1
                心跳间隔(秒)  =  30
        心跳消息发送次数阈值  =  5
                去活用户开关  =  开
                去活间隔(秒)  =  900
        心跳消息超时间隔(秒)  =  3
                迁移间隔(秒)  =  60
                核查用户开关  =  开
          惯性运行定时器(秒)  =  30
        静默路径业务迁移开关  =  使能
    静默路径业务迁移间隔(秒)  =  0
    静默路径业务回迁间隔(秒)  =  60
    静默路径状态恢复间隔(秒)  =  3600
静默路径发送偶联建立请求消息  =  使能
    流量上报消息保序优化开关  =  关
        发送偶联更新消息开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPFPFCPPARA.md`
