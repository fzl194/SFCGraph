---
id: UNC@20.15.2@MMLCommand@RMV SFCPARA
type: MMLCommand
name: RMV SFCPARA（删除SFC参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SFCPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 感知业务管理
- 感知控制面功能参数
status: active
---

# RMV SFCPARA（删除SFC参数）

## 功能

![](删除SFC参数（RMV SFCPARA）_83159238.assets/notice_3.0-zh-cn_2.png)

执行此命令，会导致SFC信息缺失，影响感知gNodeB业务。

**适用NF：AMF**

在部署感知的场景下，通过RMV SFCPARA删除SFC的参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFCINSTANCEID | SFC实例ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定SFC网元的实例ID。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~64。只允许输入十进制数字（0-9），除0之外不能以0开头。对应十进制数取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFCPARA]] · SFC参数（SFCPARA）

## 使用实例

若运营商要删除一条SFC的参数信息，SFC实例ID为1，可以用如下命令：

```
RMV SFCPARA: SFCINSTANCEID="1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SFC参数（RMV-SFCPARA）_83159238.md`
