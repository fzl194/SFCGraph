---
id: UNC@20.15.2@MMLCommand@LST NGNILRPARA
type: MMLCommand
name: LST NGNILRPARA（查询NI-LR功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGNILRPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G定位服务管理
- 紧急定位服务管理
status: active
---

# LST NGNILRPARA（查询NI-LR功能参数）

## 功能

**适用NF：AMF**

该命令用于查询指定运营商的NI-LR功能的参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于在UNC系统内唯一标识移动网络运营商。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：<br>该参数取值必须和ADD NGMNO中配置的“NOID”参数取值相同。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGNILRPARA]] · NI-LR功能参数（NGNILRPARA）

## 使用实例

查询NOID为0的NI-LR功能参数，执行命令如下：

```
%%LST NGNILRPARA: NOID=0;%%
RETCODE = 0  操作成功

结果如下
--------
                  运营商标识  =  0
    是否允许网络触发定位功能  =  否
          网络触发的定位策略  =  协议模式定位
    紧急呼叫释放是否上报位置  =  否
                    水平精度  =  19
                    响应时间  =  低时延
          是否对GMLC进行重发  =  否
                是否重选GMLC  =  否
紧急会话切换的位置连续性开关  =  否
                切换上报类型  =  源侧上报
               LCS QoS Class  =  无效值
                    描述信息  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGNILRPARA.md`
