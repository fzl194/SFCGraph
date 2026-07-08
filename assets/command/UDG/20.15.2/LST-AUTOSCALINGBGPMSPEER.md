---
id: UDG@20.15.2@MMLCommand@LST AUTOSCALINGBGPMSPEER
type: MMLCommand
name: LST AUTOSCALINGBGPMSPEER（查询BGP自动化多源邻居配置模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOSCALINGBGPMSPEER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- BGP多源peer自动化配置
status: active
---

# LST AUTOSCALINGBGPMSPEER（查询BGP自动化多源邻居配置模板）

## 功能

该命令用于查询BGP多源peer自动化配置模板。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无 |
| IPVERSION | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用来指定peer的地址族信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>默认值：无 |
| PEER4 | 对等体地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于指定用所连接对等体的接口地址。要求和ADD BGPPEER命令中的PEERADDR参数保持一致。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AUTOSCALINGBGPMSPEER]] · BGP自动化多源邻居配置模板（AUTOSCALINGBGPMSPEER）

## 使用实例

查询BGP多源peer自动化配置模板信息：

```
LST AUTOSCALINGBGPMSPEER: SERVICENAME="service1";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  服务名称  =  service1
    地址族  =  IPv4地址族
对等体地址  =  10.1.1.1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-AUTOSCALINGBGPMSPEER.md`
