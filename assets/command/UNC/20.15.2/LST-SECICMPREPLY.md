---
id: UNC@20.15.2@MMLCommand@LST SECICMPREPLY
type: MMLCommand
name: LST SECICMPREPLY（查询ICMP快回）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SECICMPREPLY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略ICMP
status: active
---

# LST SECICMPREPLY（查询ICMP快回）

## 功能

该命令用于查询ICMP快回使能配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECICMPREPLY]] · ICMP快回（SECICMPREPLY）

## 使用实例

- 查询ICMP快回使能配置：
  ```
  LST SECICMPREPLY:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
       RU名称  =  VNODE_VNRS_VNFC_IPU_0064
     使能标记  =  是 
  (结果个数 = 1)
  ---    END
  ```
- 查询指定条件ICMP快回使能配置：
  ```
  LST SECICMPREPLY:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
      RU名称  =  VNODE_VNRS_VNFC_IPU_0064
    使能标记  =  是 
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询ICMP快回（LST-SECICMPREPLY）_49802478.md`
