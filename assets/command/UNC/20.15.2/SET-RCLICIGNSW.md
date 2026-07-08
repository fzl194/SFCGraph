---
id: UNC@20.15.2@MMLCommand@SET RCLICIGNSW
type: MMLCommand
name: SET RCLICIGNSW（设置注册中心用户数license忽略开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RCLICIGNSW
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- License管理
status: active
---

# SET RCLICIGNSW（设置注册中心用户数license忽略开关）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF/VLR到注册中心进行用户注册时是否忽略注册中心用户数license控制结果。开关打开时SMSF/VLR只根据“融合短信注册用户数”License项控制用户注册，当此license项未超限但注册中心用户数license超限时。

SMSF/VLR仍然向AMF/MME响应注册成功。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RCLICIGNSW |
| --- |
| FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RCLICIGNSW | 注册中心用户数license忽略开关 | 可选必选说明：必选参数<br>参数含义：该参数用户设置SMSF/VLR到注册中心注册时是否忽略。<br>注册中心用户数license控制结果。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RCLICIGNSW]] · 注册中心用户数license忽略开关（RCLICIGNSW）

## 使用实例

运营商希望SMSF/VLR到注册中心进行用户注册时忽略注册中心的Liense控制结果，执行如下命令：

```
SET RCLICIGNSW: RCLICIGNSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置注册中心用户数license忽略开关（SET-RCLICIGNSW）_54974858.md`
