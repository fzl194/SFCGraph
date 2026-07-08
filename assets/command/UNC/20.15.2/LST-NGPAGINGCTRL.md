---
id: UNC@20.15.2@MMLCommand@LST NGPAGINGCTRL
type: MMLCommand
name: LST NGPAGINGCTRL（查询5G寻呼策略控制表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPAGINGCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG寻呼策略管理
status: active
---

# LST NGPAGINGCTRL（查询5G寻呼策略控制表）

## 功能

**适用NF：AMF**

此命令用于查询当前配置的S1寻呼策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGCTRL]] · 5G寻呼策略控制表（NGPAGINGCTRL）

## 使用实例

查询NG寻呼策略控制表，执行如下命令：

```
%%LST NGPAGINGCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
                       最近GNB开关  =  OFF
            最近GNB寻呼超时时长(s)  =  3
    最近GNB寻呼超时重发次数(times)  =  0
                       邻接GNB开关  =  OFF
            邻接GNB寻呼超时时长(s)  =  3
    邻接GNB寻呼超时重发次数(times)  =  0
                    最近访问TA开关  =  OFF
        最近驻留TAI寻呼超时时长(s)  =  3
最近驻留TAI寻呼超时重发次数(times)  =  0
                        邻接TA开关  =  OFF
             邻接TA寻呼超时时长(s)  =  3
     邻接TA寻呼超时重发次数(times)  =  0
                  低移动性检查开关  =  OFF
                  GNB粘性时长(min)  =  15
                   TA粘性时长(min)  =  0
                        HO学习开关  =  OFF
                       SON学习开关  =  OFF
               Path Switch学习开关  =  OFF
                    邻接TA学习开关  =  OFF
                邻接GNB老化时间(h)  =  360
                 邻接TA老化时间(h)  =  360
                      全网寻呼开关  =  OFF
          高优先级寻呼消息处理策略  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGPAGINGCTRL.md`
