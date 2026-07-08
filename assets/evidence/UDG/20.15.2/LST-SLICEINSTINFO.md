# 显示切片实例信息（LST SLICEINSTINFO）

- [命令功能](#ZH-CN_CONCEPT_0251061264__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251061264__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0251061264__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0251061264__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0251061264__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0251061264__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0251061264)

**适用NF：UPF**

此命令用于显示切片实例信息。

#### [注意事项](#ZH-CN_CONCEPT_0251061264)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0251061264)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251061264)

无。

#### [使用实例](#ZH-CN_CONCEPT_0251061264)

查询切片实例信息：

```
LST SLICEINSTINFO:;
```

```

RETCODE = 0  操作成功

网络切片实例信息
----------------
   NsiInfo  =  test
   NSSI ID  =  0
配置域名称  =  NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0251061264)

参见ADD SLICEINSTINFO的参数说明。
