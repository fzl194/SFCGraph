---
id: UNC@20.15.2@MMLCommand@LST IPAREAGP
type: MMLCommand
name: LST IPAREAGP（查询IP区域群）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPAREAGP
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 基于位置分配IP地址管理
- IP区域群管理
status: active
---

# LST IPAREAGP（查询IP区域群）

## 功能

**适用网元：SGSN、MME**

该命令用于查询IP区域群记录。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识待查询的区域群。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPAREAGP]] · IP区域群（IPAREAGP）

## 使用实例

1. 查询标识为1的IP区域群记录：
  LST IPAREAGP: AREAID = 1;
  ```
  %%LST IPAREAGP: AREAID=1;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------       
        区域群标识  =  1
        IP区域开关  =  关闭
      漫游用户开关  =  关闭
  本网异地用户开关  =  关闭
        区域群名称  =  noname
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPAREAGP.md`
