---
id: UDG@20.15.2@MMLCommand@LST UPGLBDIAMREALM
type: MMLCommand
name: LST UPGLBDIAMREALM（查询全局Diameter域）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPGLBDIAMREALM
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter Realm
- 全局Realm
status: active
---

# LST UPGLBDIAMREALM（查询全局Diameter域）

## 功能

**适用NF：UPF**

该命令用于查询全局Diameter域。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局Diameter域所属的Diameter应用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：根据实际应用场景选择对应的枚举值。 |

## 操作的配置对象

- [全局Diameter域（UPGLBDIAMREALM）](configobject/UDG/20.15.2/UPGLBDIAMREALM.md)

## 使用实例

- 查询全局Diameter域与SWM应用的绑定关系：
  ```
  LST UPGLBDIAMREALM: APPLICATION=SWM;
  ```
  ```

  RETCODE = 0  操作成功
  全局Diameter域名
  ----------------
                    Diameter应用  =  SWM
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  test.huawei.com
  (结果个数 = 1)
  ---    END
  ```
- 查询所有全局Diameter域的绑定关系：
  ```
  LST UPGLBDIAMREALM:;
  ```
  ```

  RETCODE = 0  操作成功
  全局Diameter域名
  ----------------
                    Diameter应用  =  SWM
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  test.huawei.com
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局Diameter域（LST-UPGLBDIAMREALM）_97314567.md`
