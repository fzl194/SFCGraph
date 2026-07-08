---
id: UNC@20.15.2@MMLCommand@LST UPSELECTFLAG
type: MMLCommand
name: LST UPSELECTFLAG（查询UPF选择条件开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPSELECTFLAG
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF选择条件开关
status: active
---

# LST UPSELECTFLAG（查询UPF选择条件开关）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询SMF的整机UPF选择条件开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPSELECTFLAG]] · UPF选择条件开关（UPSELECTFLAG）

## 使用实例

查询所有UPF选择条件开关： LST UPSELECTFLAG:;

```
%%LST UPSELECTFLAG:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                     I-UPF选择的APN开关  =  关
         基于ULIForSGW位置选择SGW-U开关  =  关
                    AMBR聚合UPF选择开关  =  关
                        UPF选择临时抑制  =  开	
            基于用户漫游类型选择UPF开关  =  关	   
                     5G LAN UPF选择开关  =  本地能力		   
                        租约UPF选择开关  =  开
                      位置区UPF优选开关  =  开			   
              基于位置优选主锚点UPF开关  =  关	 
                        过载UPF过滤开关  =  开
                      优先级优选UPF开关  =  开
                高优先级容许过载UPF开关  =  关
                    基于负载优选UPF开关  =  开
    基于UPF上报的APN锁定信息选择UPF开关  =  关
基于UPF上报的APN锁定信息选择接入UPF开关  =  关
(结果个数 = 1)

---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPSELECTFLAG.md`
