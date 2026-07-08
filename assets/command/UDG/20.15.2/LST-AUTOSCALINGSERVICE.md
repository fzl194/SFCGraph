---
id: UDG@20.15.2@MMLCommand@LST AUTOSCALINGSERVICE
type: MMLCommand
name: LST AUTOSCALINGSERVICE（查询自动化配置参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOSCALINGSERVICE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 服务信息
status: active
---

# LST AUTOSCALINGSERVICE（查询自动化配置参数）

## 功能

该命令用于查询接口自动化配置模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口自动化配置服务模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AUTOSCALINGSERVICE]] · 自动化配置参数（AUTOSCALINGSERVICE）

## 使用实例

显示“SERVICENAME”为“service4”的接口自动化配置模板：

```
LST AUTOSCALINGSERVICE:SERVICENAME="service4";
```

```

RETCODE = 0  操作成功

结果如下:
-------------------------
                   服务名称   =  service4
                VPN实例名称   =  vpn4
                     地址族   =  IPv4地址族
          自动化配置接口类型  =  虚拟网卡
            以太Trunk模板ID   =  0
                 虚拟网卡ID   =  4
                    VLAN ID   =  4
                   起始地址   =  10.1.1.1
                   结束地址   =  10.1.1.10
             地址池掩码长度   =  24
                   使能OSPF   =  是
                 OSPF进程ID   =  1
                 OSPF区域ID   =  0.0.0.0
                 OSPF实例ID   =  NULL
                   OSPF开销   =  4
       入方向的流量策略名称   =  in
   入方向的流量策略链接标记   =  FALSE
       出方向的流量策略名称   =  out
   出方向的流量策略链接标记   =  TRUE
               最大传输单元   =  200
邻居发送Hello包时间间隔（s）  =  50
         邻居失效的时间（s）  =  70
                   引流模式   =  路由模式
           IPv4地址分配方式   =  用户配置方式
           IPv6地址分配方式   =  NULL
               网络分组标识   =  1
             备用路由组标记   =  TRUE
          简单流分类QoS策略   =  default
             使能OSPF进程组   =  FALSE
               OSPF进程组ID   =  0
                   地址模式   =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询自动化配置参数（LST-AUTOSCALINGSERVICE）_50120950.md`
