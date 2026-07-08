---
id: UNC@20.15.2@MMLCommand@LST AMFFUNCTION
type: MMLCommand
name: LST AMFFUNCTION（查询AMF功能实例信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFFUNCTION
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# LST AMFFUNCTION（查询AMF功能实例信息）

## 功能

**适用NF：AMF**

本命令用于查看AMF功能实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFFUNCTION]] · AMF功能实例信息（AMFFUNCTION）

## 使用实例

查看AMFFUNCTION实例信息。

```
%%LST AMFFUNCTION:;%%
RETCODE = 0  操作成功

结果如下
------------------------
             NF实例号  =  b7b621d82dfb4a009d492491bd9d72a4
            NF实例描述  =  AMF1
          管理状态  =  未锁定
          运行状态  =  运行
               FQDN  =  amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
         最大注册用户数  =  500000
               相对容量  =  200
        最大支持基站数 =  50000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFFUNCTION.md`
