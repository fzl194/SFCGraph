---
id: UNC@20.15.2@MMLCommand@LST CCT
type: MMLCommand
name: LST CCT（查询融合计费模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCT
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
- 融合计费模板
status: active
---

# LST CCT（查询融合计费模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询融合计费模板（Converged Charging Template），用于配置融合计费相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置融合计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCT]] · 融合计费模板（CCT）

## 使用实例

查询名为“test”的融合计费模板信息：

```
%%LST CCT:;%%
RETCODE = 0  操作成功

结果如下
--------
                          融合计费模板名称  =  global
                           CHF交互使能开关  =  激活发送
                                初始RG个数  =  5
                    CHF交互等待CHF响应开关  =  使能
                                    RG来源  =  缺省配置
                    配额空闲时间门限值(秒)  =  0
                     流量阈值触发百分比(%)  =  20
                     时间阈值触发百分比(%)  =  20
                     事件阈值触发百分比(%)  =  20
                      在线配额有效时长(分)  =  30
                          计费条件改变阈值  =  3
                           PDU流量阈值(MB)  =  500
                         PDU时长阈值(分钟)  =  30
                        业务级流量阈值(MB)  =  500
                      业务级时长阈值(分钟)  =  30
                            QF流量阈值(MB)  =  500
                          QF时长阈值(分钟)  =  30
                  最终配额动作指示终结方式  =  阻塞业务
                                FH处理动作  =  去活PDU会话
                      支持failover使能开关  =  不使能
                          failback使能开关  =  使能
                          Tx定时器时长(秒)  =  3
                        用户保持时长(分钟)  =  30
                    用户保持调整时长(分钟)  =  30
                  融合计费自动恢复功能开关  =  不使能
               融合计费自动恢复间隔 (分钟)  =  20
                        业务停止时长(分钟)  =  60
                                  时间格式  =  本地时间
    Update消息触发业务放通结束计费会话开关  =  不使能
                    最大携带的业务容器数量  =  100
RAN-SecondaryRAT-Usage-Report上报CHF的阈值  =  100
                      最大可使用的业务个数  =  60
            QHT超时触发的容器中Trigger的值  =  上报QHT
          漫游用户最终配额动作指示终结方式  =  阻塞业务
                 漫游用户的PDU流量阈值(MB)  =  0
 会话层异常返回码动作为Block时阻塞免费业务  =  不阻塞
                            无配额更新开关  =  使能
                           SCP故障重选开关  =  SCP故障不进行重选
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CCT.md`
