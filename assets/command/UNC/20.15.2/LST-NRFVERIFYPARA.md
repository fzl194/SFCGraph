---
id: UNC@20.15.2@MMLCommand@LST NRFVERIFYPARA
type: MMLCommand
name: LST NRFVERIFYPARA（查询NF属性冲突核验参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFVERIFYPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF属性冲突核验
status: active
---

# LST NRFVERIFYPARA（查询NF属性冲突核验参数）

## 功能

**适用NF：NRF**

该命令用于查询NF属性冲突核验参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFVERIFYPARA]] · NF属性冲突核验参数（NRFVERIFYPARA）

## 使用实例

查询NF属性冲突核验参数：

```
LST NRFVERIFYPARA:;
%%LST NRFVERIFYPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
                     起始位置  =  4
                         长度  =  3
             NF间冲突核验属性  =  IMSI&MSISDN
NF和跨NRF路由数据冲突核验属性  =  IMSI&MSISDN
                 每秒核验步长  =  10
             核验超时时长(秒)  =  60
       核验结果老化时长(分钟)  =  5
     最大核验失败属性元素个数  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF属性冲突核验参数（LST-NRFVERIFYPARA）_35636455.md`
