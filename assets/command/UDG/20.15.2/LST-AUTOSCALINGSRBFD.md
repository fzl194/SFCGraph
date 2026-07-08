---
id: UDG@20.15.2@MMLCommand@LST AUTOSCALINGSRBFD
type: MMLCommand
name: LST AUTOSCALINGSRBFD（查询静态路由的动态BFD自动化配置模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOSCALINGSRBFD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 静态路由的动态BFD自动化配置
status: active
---

# LST AUTOSCALINGSRBFD（查询静态路由的动态BFD自动化配置模板）

## 功能

该命令用于查询静态路由的动态BFD自动化配置模板。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| IPVERSION | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用来表示IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>- IPv6：IPv6地址族。<br>默认值：IPv4 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AUTOSCALINGSRBFD]] · 静态路由的动态BFD自动化配置模板（AUTOSCALINGSRBFD）

## 使用实例

查询一个静态路由的动态BFD自动化配置模板：

```
LST AUTOSCALINGSRBFD:SERVICENAME="abc";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
         服务名称   =  abc
           地址族   =  IPv4地址族
最小接收间隔（ms）  =  200
最小发送间隔（ms）  =  200
         检测倍数   =  3
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-AUTOSCALINGSRBFD.md`
