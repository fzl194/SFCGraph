---
id: UNC@20.15.2@MMLCommand@LST NGDNSCACHE
type: MMLCommand
name: LST NGDNSCACHE（查询DNS缓存参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGDNSCACHE
command_category: 查询类
applicable_nf:
- SGW-C
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端缓存管理
status: active
---

# LST NGDNSCACHE（查询DNS缓存参数）

## 功能

**适用NF：SGW-C、AMF**

该命令用于查询DNS缓存参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGDNSCACHE]] · DNS缓存（NGDNSCACHE）

## 使用实例

使用以下命令查询DNS缓存参数：

```
%%LST NGDNSCACHE:;%%
RETCODE = 0  操作成功

结果如下
--------
              缓存使能  =  TRUE
          最大FQDN数量  =  4
最大主机名控制节点数量  =  8
        最大主机名数量  =  10
 写缓存最大速率(次/秒)  =  6
   FQDN扫描速率(个/秒)  =  5
          老化时长(秒)  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGDNSCACHE.md`
