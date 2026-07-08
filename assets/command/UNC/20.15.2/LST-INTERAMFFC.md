---
id: UNC@20.15.2@MMLCommand@LST INTERAMFFC
type: MMLCommand
name: LST INTERAMFFC（查询Inter-AMF流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INTERAMFFC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 拥塞控制
- Inter-AMF流控参数
status: active
---

# LST INTERAMFFC（查询Inter-AMF流控参数）

## 功能

**适用NF：AMF**

该命令用于查询Inter-AMF接入流控功能的相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@INTERAMFFC]] · Inter-AMF流控参数（INTERAMFFC）

## 使用实例

查询Inter-AMF单POD接入流控参数，执行如下命令：

```
%%LST INTERAMFFC:;%%
RETCODE = 0  操作成功

结果如下
--------
           Inter-AMF接入流控功能开关  =  开启
Registration Request流控阈值作用范围  =  单POD
 Registration Request速率门限(个/秒)  =  300
     Service Request流控阈值作用范围  =  单POD
      Service Request速率门限(个/秒)  =  300
                      告警上报周期数  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-INTERAMFFC.md`
