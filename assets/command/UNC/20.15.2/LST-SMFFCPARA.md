---
id: UNC@20.15.2@MMLCommand@LST SMFFCPARA
type: MMLCommand
name: LST SMFFCPARA（查询SMF自保流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFFCPARA
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
- 接入管理运维
- 流控管理
- SMF流控参数
status: active
---

# LST SMFFCPARA（查询SMF自保流控参数）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询SMF自保流控原因值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [SMF自保流控参数（SMFFCPARA）](configobject/UNC/20.15.2/SMFFCPARA.md)

## 使用实例

查询全部的SMF自保流程控制参数:

```
%%LST SMFFCPARA:;%%
            RETCODE = 0  操作成功

            结果如下
            --------
            5G会话创建流控原因值  =  26
            4G会话创建流控原因值  =  73
            2/3G PDP激活流控原因值  =  204
            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMF自保流控参数（LST-SMFFCPARA）_01214230.md`
