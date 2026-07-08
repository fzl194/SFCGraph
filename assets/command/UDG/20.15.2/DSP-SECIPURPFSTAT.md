---
id: UDG@20.15.2@MMLCommand@DSP SECIPURPFSTAT
type: MMLCommand
name: DSP SECIPURPFSTAT（显示URPF丢弃报文计数信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SECIPURPFSTAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- URPF统计
status: active
---

# DSP SECIPURPFSTAT（显示URPF丢弃报文计数信息）

## 功能

该命令用来查看IPv4或IPv6 URPF检查丢弃报文的统计计数。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| SECPROTOFAMILY | 安全协议族 | 可选必选说明：必选参数<br>参数含义：安全协议族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4类型。<br>- ipv6：IPv6类型。<br>默认值：无 |

## 操作的配置对象

- [URPF丢弃报文计数信息（SECIPURPFSTAT）](configobject/UDG/20.15.2/SECIPURPFSTAT.md)

## 使用实例

- 查看设备上所有IPv4 URPF检查丢弃报文的统计计数：
  ```
  DSP SECIPURPFSTAT:SECPROTOFAMILY=ipv4;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
  RU名称                      安全协议族            URPF丢弃报文计数

  VNODE_VNRS_VNFC_IPU_0064    IPv4           0                     
  VNODE_VNRS_VNFC_IPU_0065    IPv4           0                     
  (结果个数 = 2)
  ---    END
  ```
- 查看设备中一个VNRS_IP_RU上IPv4 URPF检查丢弃报文的统计计数：
  ```
  DSP SECIPURPFSTAT:RUNAME="VNODE_VNRS_VNFC_IPU_0064",SECPROTOFAMILY=ipv4;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
                  RU名称  =  VNODE_VNRS_VNFC_IPU_0064
              安全协议族  =  IPv4
        URPF丢弃报文计数  =  0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示URPF丢弃报文计数信息（DSP-SECIPURPFSTAT）_50121378.md`
