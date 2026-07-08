---
id: UDG@20.15.2@MMLCommand@LST SNSSAIUPINTF
type: MMLCommand
name: LST SNSSAIUPINTF（查询网络切片和逻辑接口绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SNSSAIUPINTF
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片与逻辑接口绑定关系配置
status: active
---

# LST SNSSAIUPINTF（查询网络切片和逻辑接口绑定关系）

## 功能

**适用NF：UPF**

该命令用于查询指定的网络切片选择标识绑定的N3逻辑接口信息。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片/服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用来设置切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：无 |
| SD | 切片区分码 | 可选必选说明：可选参数<br>参数含义：该参数用来指定切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，每个字符必须为0~9的数字或a~f/A-F的字母。<br>默认值：无<br>配置原则：该参数必须是长度为6的字符串。如果S-NSSAI无SD，需配置为全F。 |

## 操作的配置对象

- [网络切片和逻辑接口绑定关系（SNSSAIUPINTF）](configobject/UDG/20.15.2/SNSSAIUPINTF.md)

## 使用实例

- 获取当前UPF配置的所有网络切片选择标识跟N3逻辑接口的绑定关系：
  ```
  LST SNSSAIUPINTF:;
  ```
  ```

  RETCODE = 0 操作成功

  网络切片和逻辑接口绑定信息
  -------------------------------------------
    切片/服务类型  =  1
       切片区分码  =  123456
   N3逻辑接口名称  =  n3if1/1/2
  (结果个数 =  1)

  ---    END
  ```
- 获取指定网络切片选择标识跟N3逻辑接口的绑定关系：
  ```
  LST SNSSAIUPINTF: SST=1, SD="123456";
  ```
  ```

  RETCODE = 0 操作成功

  网络切片和逻辑接口绑定信息
  -------------------------------------------
    切片/服务类型  =  1
       切片区分码  =  123456
   N3逻辑接口名称  =  n3if1/1/2
  (结果个数 =  1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询网络切片和逻辑接口绑定关系（LST-SNSSAIUPINTF）_51061268.md`
