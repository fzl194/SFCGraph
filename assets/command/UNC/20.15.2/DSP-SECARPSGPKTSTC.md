---
id: UNC@20.15.2@MMLCommand@DSP SECARPSGPKTSTC
type: MMLCommand
name: DSP SECARPSGPKTSTC（显示ARP双向分离报文统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SECARPSGPKTSTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- ARP双向分离
status: active
---

# DSP SECARPSGPKTSTC（显示ARP双向分离报文统计）

## 功能

该命令用于显示ARP双向分离报文统计信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECARPSGPKTSTC]] · ARP双向分离报文统计（SECARPSGPKTSTC）

## 使用实例

- 显示ARP双向分离报文统计信息：
  ```
  DSP SECARPSGPKTSTC:;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  RU 名称                     ARP请求上送CPU报文个数    ARP请求丢弃报文个数    ARP应答发送报文个数    ARP应答上送CPU报文个数    ARP应答丢弃报文个数

  VNODE_VNRS_VNFC_IPU_0066    3                         0                      0                      0                         0
  VNODE_VNRS_VNFC_IPU_0067    0                         0                      0                      0                         0
  (结果个数 = 2)
  ---    END
  ```
- 显示指定资源单元的ARP双向分离报文统计信息：
  ```
  DSP SECARPSGPKTSTC:RUNAME="VNODE_VNRS_VNFC_IPU_0066";
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
                 RU 名称  =  VNODE_VNRS_VNFC_IPU_0066
  ARP请求上送CPU报文个数  =  3
     ARP请求丢弃报文个数  =  0
     ARP应答发送报文个数  =  0
  ARP应答上送CPU报文个数  =  0
     ARP应答丢弃报文个数  =  0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示ARP双向分离报文统计（DSP-SECARPSGPKTSTC）_49961466.md`
