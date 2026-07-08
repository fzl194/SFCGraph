---
id: UNC@20.15.2@MMLCommand@LST AREAGP
type: MMLCommand
name: LST AREAGP（查询区域群）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AREAGP
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
- 区域漫游限制管理
- 区域群管理
status: active
---

# LST AREAGP（查询区域群）

## 功能

**适用网元：SGSN、MME**

此命令用于查询区域群记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：可选参数<br>参数含义：待查询的区域群标识。<br>数据来源：整网规划<br>取值范围：1～50<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AREAGP]] · 区域群（AREAGP）

## 使用实例

1. 不输入查询条件，查询表中全部区域群记录属性信息：
  LST AREAGP:;
  ```
  %%LST AREAGP:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   区域群标识  区域群名称

   1           group1    
   2           group2    
  (结果个数 = 2)
  ---    END
  ```
2. 查询区域群标识为1的区域群记录：
  LST AREAGP: AREAID = 1;
  ```
  %%LST AREAGP: AREAID=1;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   区域群标识  =  1
   区域群名称  =  group1
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AREAGP.md`
