---
id: UNC@20.15.2@MMLCommand@LST OSPFABRSUMMARY
type: MMLCommand
name: LST OSPFABRSUMMARY（查询区域内路由聚合配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFABRSUMMARY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域内路由聚合配置
status: active
---

# LST OSPFABRSUMMARY（查询区域内路由聚合配置）

## 功能

该命令用于查询区域内路由聚合配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域ID | 可选必选说明：可选参数<br>参数含义：区域ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IPADDRESS | IP地址 | 可选必选说明：可选参数<br>参数含义：IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| ADDRESSMASK | IP地址的掩码 | 可选必选说明：可选参数<br>参数含义：IP地址的掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [区域内路由聚合配置（OSPFABRSUMMARY）](configobject/UNC/20.15.2/OSPFABRSUMMARY.md)

## 使用实例

查询区域内路由聚合配置：

```
LST OSPFABRSUMMARY:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------
        OSPF进程号  =  1
            区域ID  =  0.0.0.0
          拓扑标识  =  基础类型
            IP地址  =  10.2.2.0
      IP地址的掩码  =  255.255.255.0
      发布路由标识  =  TRUE
      使能开销配置  =  TRUE
    聚合路由的开销  =  100
      继承最小cost  =  FALSE
      生成路由黑洞  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询区域内路由聚合配置（LST-OSPFABRSUMMARY）_49961502.md`
