---
id: UNC@20.15.2@MMLCommand@DSP GTSMSTATISTICS
type: MMLCommand
name: DSP GTSMSTATISTICS（显示GTSM统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTSMSTATISTICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- GTSM
status: active
---

# DSP GTSMSTATISTICS（显示GTSM统计）

## 功能

该命令用于显示设备GTSM各协议统计计数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于查询指定资源单元的GTSM统计。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。通过DSP RU命令可以查询资源单元信息。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTSMSTATISTICS]] · GTSM统计（GTSMSTATISTICS）

## 使用实例

- 显示指定资源单元的GTSM统计信息：
  ```
  DSP GTSMSTATISTICS: RUNAME="VNODE_VNRS_VNFC_IPU_0064";
  ```
  ```

          RETCODE = 0  操作成功
          结果如下
          -------------------------
          RU名称                      协议名       报文总数   丢弃报文总数   通过报文总数
          VNODE_VNRS_VNFC_IPU_0064    BGP协议      0          0              0
          VNODE_VNRS_VNFC_IPU_0064    BGPv6协议    0          0              0
          VNODE_VNRS_VNFC_IPU_0064    OSPF协议     0          0              0
          VNODE_VNRS_VNFC_IPU_0064    OSPFv3协议   0          0              0
          (结果个数 = 4)
          ---    END
  ```
- 显示所有资源单元的GTSM统计信息：
  ```
  DSP GTSMSTATISTICS:;
  ```
  ```

          RETCODE = 0  操作成功

          结果如下
          -------------------------
          RU名称                      协议名       报文总数   丢弃报文总数   通过报文总数
          VNODE_VNRS_VNFC_IPU_0064    BGP协议      0          0              0
          VNODE_VNRS_VNFC_IPU_0064    BGPv6协议    0          0              0
          VNODE_VNRS_VNFC_IPU_0064    OSPF协议     0          0              0
          VNODE_VNRS_VNFC_IPU_0064    OSPFv3协议   0          0              0
          (结果个数 = 4)
          ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GTSMSTATISTICS.md`
