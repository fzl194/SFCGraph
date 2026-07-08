---
id: UNC@20.15.2@MMLCommand@LST POOLLA
type: MMLCommand
name: LST POOLLA（查询POOL LA配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: POOLLA
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
- 网络管理
- SGSN POOL区管理
- POOL LA配置
status: active
---

# LST POOLLA（查询POOL LA配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于查询Pool区域LAC值，或TAI与LAC的对应关系。

## 注意事项

- 此命令执行后立即生效。
- 不输入任何参数则表示查询所有信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAI | 跟踪区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个跟踪区。<br>取值范围：9～10位的十六进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区标识，标识一个位置区。<br>取值范围：4位的十六进制数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POOLLA]] · POOL LA配置信息（POOLLA）

## 使用实例

1. 查看TAI为"308010701"，LAC为"0701"的对应关系:
  LST POOLLA: TAI="308010701", LAC="0701";
  ```
  %%LST POOLLA: TAI="308010701", LAC="0701";%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
     起始TAI  =  308010701
     终止TAI  =  308010701
  位置区域码  =  0701
  (结果个数 = 1)
  ---    END
  ```
2. 查看系统中所有的TAI与LAC对应关系：
  LST POOLLA:;
  ```
  %%LST POOLLA:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   起始TAI    终止TAI    位置区域码      

   308010701  308010701  0701
   308010702  308010702  0701
   308014101  308014103  0702
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-POOLLA.md`
