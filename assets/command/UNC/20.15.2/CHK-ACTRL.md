---
id: UNC@20.15.2@MMLCommand@CHK ACTRL
type: MMLCommand
name: CHK ACTRL（检查链路分配信息）
nf: UNC
version: 20.15.2
verb: CHK
object_keyword: ACTRL
command_category: 调测类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 接入控制
status: active
---

# CHK ACTRL（检查链路分配信息）

## 功能

**适用NF：NCG**

用于查看CGF模块为对端分配AP的具体情况。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |

## 操作的配置对象

- [接入控制（ACTRL）](configobject/UNC/20.15.2/ACTRL.md)

## 使用实例

查询对端的AP分配情况，示例如下：

```
CHK ACTRL:; 
RETCODE = 0  操作成功。

结果如下:
--------
接入控制标识    协议类型    接入网元分组标识    Ga IP地址         Ga端口号        AP模块编号 

actrl           GTP'        PS2                 192.168.99.78       6009             651        
actrll          GTP'        PS1                 192.168.99.78       6001             641        
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/检查链路分配信息（CHK-ACTRL）_51174237.md`
